package ru.arkuzmin.simulation.model;

import sim.engine.SimState;
import sim.engine.Steppable;
import sim.field.continuous.Continuous2D;
import sim.field.network.Edge;
import sim.util.Bag;
import sim.util.Double2D;
import sim.util.MutableDouble2D;

public class Student implements Steppable {

	private static final long serialVersionUID = 1362850325594961169L;
	
	private static final double MAX_AGITATION = 10.0;
	private static final double MAX_SATISFACTION = 0.0;
	
	private String name;
	private double xPosition;
	private double yPosition;
	
	public static final double MAX_FORCE = 3.0;
	
	public Student() {
		this.name = "Неизвестный";
	}
	
	public Student(String name) {
		this.name = name;
	}
	
	public String getName() {
		return this.name;
	}
	
	public double getXPosition() {
		return xPosition;
	}
	
	public double getYPosition() {
		return yPosition;
	}
	
	@Override
	public String toString() {
		return name + " [" + getSatisfaction() + "]";
	}
	
	double friendsClose = MAX_SATISFACTION;
	double enemiesCloser = MAX_AGITATION;

	/**
	 * Возвращает текущую удовлетворенность студента.
	 * @return
	 */
	public int getSatisfaction() {
		double agitation = getAgitation();
		double agPer = agitation * 100.0 / MAX_AGITATION;
		double satPer = 100.0 - agPer;
		
		return (int) satPer;
	}
	
	public double getAgitation() {
		double agitation = friendsClose + enemiesCloser;
		if (agitation > MAX_AGITATION) {
			agitation = MAX_AGITATION;
		}
		return agitation;
	}

	@Override
	public void step(SimState state) {
		Students students = (Students) state;
		Continuous2D yard = students.getYard();

		Double2D me = students.getYard().getObjectLocation(this);
		MutableDouble2D sumForces = new MutableDouble2D();

		friendsClose = enemiesCloser = 0.0;
		
		// Проходим по списку друзей и определяем желание быть рядом с ними
		MutableDouble2D forceVector = new MutableDouble2D();
		Bag out = students.getBuddies().getEdges(this, null);
		int len = out.size();
		for (int buddy = 0; buddy < len; buddy++) {
			Edge e = (Edge) (out.get(buddy));
			// Показатель "дружбы" между студентами
			double buddiness = Double.parseDouble(String.valueOf(e.info));
			Double2D him = students.getYard().getObjectLocation(e.getOtherNode(this));
			
			// Если студент - друг
			if (buddiness >= 0)	{
				forceVector.setTo((him.x - me.x) * buddiness, (him.y - me.y) * buddiness);
				if (forceVector.length() > MAX_FORCE) {
					forceVector.resize(MAX_FORCE);
				}
				friendsClose += forceVector.length();
			
			// Если студент - не друг
			} else {
				forceVector.setTo((him.x - me.x) * buddiness, (him.y - me.y) * buddiness);
				if (forceVector.length() > MAX_FORCE) {
					forceVector.resize(0.0);
				} else if (forceVector.length() > 0) {
					forceVector.resize(MAX_FORCE - forceVector.length()); 
				}
				enemiesCloser += forceVector.length();
			}
			
			sumForces.addIn(forceVector);
		}

		// Добавляем вектор к учителю (чтобы студент не отходил слишком далеко от центра)
		sumForces.addIn(new Double2D((yard.width * 0.5 - me.x) * students.getForceToSchoolMultiplier(), 
									 (yard.height * 0.5 - me.y) * students.getForceToSchoolMultiplier()));

		// Добавляем вектор случайного направления движения студента
		sumForces.addIn(new Double2D(students.getRandomMultiplier() * (students.random.nextDouble() * 1.0 - 0.5),
				                     students.getRandomMultiplier() * (students.random.nextDouble() * 1.0 - 0.5)));

		sumForces.addIn(me);

		// Обновляем текущее положение студента
		xPosition = me.x + yard.width * 0.5 ;
		yPosition = me.y + yard.height * 0.5 ;
		students.getYard().setObjectLocation(this, new Double2D(sumForces));
	}

}
