<%@ WebService Language="C#" Class="CorpusGreetingService" %>
using System.Web.Services;
[WebService(Namespace="urn:corpus:greeting")]
public class CorpusGreetingService : WebService {
 [WebMethod] public string Hello() { return "Hello, World!"; }
}
