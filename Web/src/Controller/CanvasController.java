package Controller;
import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.util.stream.Collectors;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.apache.tomcat.util.codec.binary.Base64;

/**
 * Servlet implementation class CanvasController
 */
@WebServlet("/CanvasController")
public class CanvasController extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public CanvasController() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#service(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		System.out.println("service...\n");
		uploadImage(request, response);
	}

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		service(request, response);
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		service(request, response);
	}
	protected void uploadImage(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		String test = request.getReader().lines().collect(Collectors.joining(System.lineSeparator()));
	    //System.out.println(test);
	    byte[] bImg64 = test.getBytes();
	    byte[] bImg = Base64.decodeBase64(bImg64);
	    File folder = new File("C:\\Users\\LKina\\Documents\\GitHub\\Korean-Recognition\\Python\\image-data\\user-input\\");
	    File[] listOfFiles = folder.listFiles();
	    String PATH = "C:\\Users\\LKina\\Documents\\GitHub\\Korean-Recognition\\Python\\image-data\\user-input\\img";
	    System.out.println("PATH: " + PATH);
	    System.out.println("listOFFiles: " + listOfFiles.length);
	    System.out.println(PATH + listOfFiles.length + ".png");
	    FileOutputStream fos = new FileOutputStream( PATH + listOfFiles.length + ".png");
	    fos.write(bImg);
	    fos.close();
	}
}
