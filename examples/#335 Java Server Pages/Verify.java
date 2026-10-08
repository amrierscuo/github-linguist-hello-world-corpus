import java.nio.file.*;
import java.net.*;
import java.net.http.*;
import java.time.Duration;
import org.apache.catalina.*;
import org.apache.catalina.startup.Tomcat;
import org.apache.jasper.servlet.*;

public class Verify {
    public static void main(String[] args) throws Exception {
        Tomcat server = new Tomcat();
        server.setBaseDir(args[0]);
        server.setHostname("127.0.0.1");
        server.setPort(0);
        server.getConnector().setProperty("address", "127.0.0.1");
        Context context = server.addContext("", Path.of(".").toAbsolutePath().toString());
        context.addServletContainerInitializer(new JasperInitializer(), null);
        Wrapper jsp = Tomcat.addServlet(context, "jsp", new JspServlet());
        jsp.addInitParameter("fork", "false");
        jsp.addInitParameter("compilerSourceVM", "17");
        jsp.addInitParameter("compilerTargetVM", "17");
        context.addServletMappingDecoded("*.jsp", "jsp");
        try {
            server.start();
            int port = server.getConnector().getLocalPort();
            HttpClient client = HttpClient.newBuilder().connectTimeout(Duration.ofSeconds(5)).build();
            HttpRequest request = HttpRequest.newBuilder(URI.create("http://127.0.0.1:" + port + "/hello.jsp")).timeout(Duration.ofSeconds(15)).build();
            HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
            if (response.statusCode() != 200 || !response.body().equals("Hello, World!\n")) throw new AssertionError(response.statusCode() + ": " + response.body());
            if (!response.headers().firstValue("content-type").orElse("").startsWith("text/plain")) throw new AssertionError("unexpected content type");
            System.out.print(response.body());
        } finally {
            server.stop();
            server.destroy();
        }
    }
}
