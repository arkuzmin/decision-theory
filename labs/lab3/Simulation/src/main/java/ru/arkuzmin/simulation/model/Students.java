package ru.arkuzmin.simulation.model;

import java.util.LinkedList;
import java.util.List;
import java.util.Properties;

import sim.engine.SimState;
import sim.field.continuous.Continuous2D;
import sim.field.network.Network;
import sim.util.Bag;
import sim.util.Double2D;

public class Students extends SimState {

	private static final long serialVersionUID = -4294660822534485141L;
	private static double forceToSchoolMultiplier;
	private static double randomMultiplier;
	private static List<String> students;
	private Network buddies = new Network(false);
	private Continuous2D yard = new Continuous2D(1, 100, 100);
	private static Properties studentProps = PropertiesLoader.loadProperties("students.properties");
	
	/**
	 * »нициализаци€ студентов из файла
	 */
	static {
		// »нициализируем список студентов
		students = new LinkedList<String>();
		String studentNames = studentProps.getProperty("students");
		String[] names = studentNames.split(",");
		for (String name : names) {
			students.add(name);
		}
		
		// »нициализируем действующие силы
		randomMultiplier = Double.parseDouble(studentProps.getProperty("randomMultiplier"));
		forceToSchoolMultiplier = Double.parseDouble(studentProps.getProperty("forceToSchoolMultiplier"));
	}
	
	public int getNumStudends() {
		return students.size();
	}

	public Network getBuddies() {
		return buddies;
	}

	public double getForceToSchoolMultiplier() {
		return forceToSchoolMultiplier;
	}

	public double getRandomMultiplier() {
		return randomMultiplier;
	}

	public Continuous2D getYard() {
		return yard;
	}

	public Students(long seed) {
		super(seed);
	}

	public void start() {
		super.start();

		yard.clear();
		buddies.clear();

		// —лучайным образом распредел€ем студентов
		for (String name : students) {
			Student student = new Student(name);
			yard.setObjectLocation(student, new Double2D(yard.getWidth() * 0.5 + random.nextDouble() - 0.5, 
														 yard.getHeight() * 0.5 + random.nextDouble() - 0.5));

			buddies.addNode(student);
			schedule.scheduleRepeating(student);
		}

		// –аспредел€ем отношени€ между студентами
		Bag students = buddies.getAllNodes();
		for (int i = 0; i < students.size(); i++) {
			Object student = students.get(i);
			// с кем студент дружит
			Object studentB = null;
			do {
				studentB = students.get(random.nextInt(students.numObjs));
			} while (student == studentB);
			double buddiness = random.nextDouble();
			buddies.addEdge(student, studentB, String.valueOf(buddiness));
			
			// с кем студент не дружит
			do {
				studentB = students.get(random.nextInt(students.numObjs));
			} while (student == studentB);
			buddiness = random.nextDouble();
			buddies.addEdge(student, studentB, new Double(-buddiness));
		}

	}
}
