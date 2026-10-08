using System;
using System.IO;
using System.Text;
using System.Web;
public class CorpusGreetingHandler : IHttpHandler {
 public bool IsReusable { get { return true; } }
 public void ProcessRequest(HttpContext context) {
  context.Response.ContentType = "text/plain";
  context.Response.ContentEncoding = Encoding.UTF8;
  string path = context.Server.MapPath("~/hello.axd");
  context.Response.Write(File.ReadAllText(path, Encoding.UTF8));
 }
}
