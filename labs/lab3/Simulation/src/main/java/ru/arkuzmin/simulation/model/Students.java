package ru.arkuzmin.simulation.model;

import sim.engine.SimState;
import sim.engine.Steppable;
import sim.field.continuous.Continuous2D;
import sim.field.network.Network;
import sim.util.Bag;
import sim.util.Double2D;

public class Students extends SimState {

	private static final long serialVersionUID = -4294660822534485141L;

	double forceToSchoolMultiplier = 0.01;
	double randomMultiplier = 0.1;

	public Continuous2D yard = new Continuous2D(1, 100, 100);

	public double TEMPERING_CUT_DOWN = 0.99;
	public double TEMPERING_INITIAL_RANDOM_MULTIPLIER = 10.0;
	public boolean tempering = true;

	public boolean isTempering() {
		return tempering;
	}

	public void setTempering(boolean val) {
		tempering = val;
	}

	public int numStudends = 50;
	public Network buddies = new Network(false);

	public Students(long seed) {
		super(seed);
	}

	public void start() {
		super.start();

		// add the tempering agent
		if (tempering) {
			randomMultiplier = TEMPERING_INITIAL_RANDOM_MULTIPLIER;
			schedule.scheduleRepeating(schedule.EPOCH, 1, new Steppable() {
				public void step(SimState state) {
					if (tempering)
						randomMultiplier *= TEMPERING_CUT_DOWN;
				}
			});
		}

		yard.clear();
		buddies.clear();

		for (int i = 0; i < numStudends; i++) {
			Student student = new Student();
			yard.setObjectLocation(student, new Double2D(yard.getWidth() * 0.5
					+ random.nextDouble() - 0.5, yard.getHeight() * 0.5
					+ random.nextDouble() - 0.5));

			buddies.addNode(student);
			schedule.scheduleRepeating(student);
		}

		// define like/dislike relationships
		Bag students = buddies.getAllNodes();
		for (int i = 0; i < students.size(); i++) {
			Object student = students.get(i);
			// who does he like?
			Object studentB = null;
			do
				studentB = students.get(random.nextInt(students.numObjs));
			while (student == studentB);
			double buddiness = random.nextDouble();
			buddies.addEdge(student, studentB, new Double(buddiness));
			// who does he dislike?
			do
				studentB = students.get(random.nextInt(students.numObjs));
			while (student == studentB);
			buddiness = random.nextDouble();
			buddies.addEdge(student, studentB, new Double(-buddiness));
		}

	}

	public static void main(String[] args) {
		doLoop(Students.class, args);
		System.exit(0);
	}
}
