<%@ WebHandler Language="C#" Class="CorpusGreetingHandler" %>
using System.Web;
public class CorpusGreetingHandler : IHttpHandler {
 public void ProcessRequest(HttpContext context) { context.Response.ContentType="text/plain"; context.Response.Write("Hello, World!"); }
 public bool IsReusable { get { return true; } }
}
