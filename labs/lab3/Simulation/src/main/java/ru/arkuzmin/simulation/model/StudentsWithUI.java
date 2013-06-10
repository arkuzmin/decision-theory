package ru.arkuzmin.simulation.model;

import java.awt.Color;
import java.awt.Graphics2D;

import javax.swing.JFrame;

import sim.display.Console;
import sim.display.Controller;
import sim.display.Display2D;
import sim.display.GUIState;
import sim.engine.SimState;
import sim.portrayal.DrawInfo2D;
import sim.portrayal.continuous.ContinuousPortrayal2D;
import sim.portrayal.network.NetworkPortrayal2D;
import sim.portrayal.network.SimpleEdgePortrayal2D;
import sim.portrayal.network.SpatialNetwork2D;
import sim.portrayal.simple.CircledPortrayal2D;
import sim.portrayal.simple.LabelledPortrayal2D;
import sim.portrayal.simple.MovablePortrayal2D;
import sim.portrayal.simple.OvalPortrayal2D;

public class StudentsWithUI extends GUIState {

	private Display2D display;
	private JFrame displayFrame;
	private ContinuousPortrayal2D yardPortrayal = new ContinuousPortrayal2D();
	private NetworkPortrayal2D buddiesPortrayal = new NetworkPortrayal2D();

	public StudentsWithUI(SimState state) {
		super(state);
	}

	public static void main(String[] args) {
		StudentsWithUI vid = new StudentsWithUI();
		Console c = new Console(vid);
		c.setVisible(true);
	}

	public static String getName() {
		return "Распределение студентов";
	}

	public StudentsWithUI() {
		super(new Students(System.currentTimeMillis()));
	}

	public void start() {
		super.start();
		setupPortrayals();
	}

	public void load(SimState state) {
		super.load(state);
		setupPortrayals();
	}

	public void setupPortrayals() {
		Students students = (Students) state;
		// Настройки отрисовки
		yardPortrayal.setField(students.getYard());
		yardPortrayal.setPortrayalForAll(new MovablePortrayal2D(
				new CircledPortrayal2D(new LabelledPortrayal2D(
						new OvalPortrayal2D(3) {

							private static final long serialVersionUID = 6979036146652279170L;

							public void draw(Object object, Graphics2D graphics, DrawInfo2D info) {
								Student student = (Student) object;
								int agitationShade = (int) (student.getAgitation() * 255 / 10.0);
								if (agitationShade > 255) {
									agitationShade = 255;
								}

								paint = new Color(agitationShade, 0, 255 - agitationShade);
								super.draw(object, graphics, info);
							}
							
						}, 5.0, null, Color.black, true), 
						0, 5.0, Color.green, true)));

		buddiesPortrayal.setField(new SpatialNetwork2D(students.getYard(), students.getBuddies()));
		buddiesPortrayal.setPortrayalForAll(new SimpleEdgePortrayal2D());

		display.reset();
		display.setBackdrop(Color.white);
	}

	public void init(Controller c) {
		super.init(c);
		display = new Display2D(600, 600, this);
		display.setClipping(false);
		displayFrame = display.createFrame();
		displayFrame.setTitle("Школьный двор");
		c.registerFrame(displayFrame); 
		displayFrame.setVisible(true);
		display.attach(buddiesPortrayal, "Студенты");
		display.attach(yardPortrayal, "Связи");
	}

	public void quit() {
		super.quit();
		if (displayFrame != null) {
			displayFrame.dispose();
		}
			
		displayFrame = null;
		display = null;
	}
}
