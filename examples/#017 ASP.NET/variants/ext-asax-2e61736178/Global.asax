<%@ Application Language="C#" %>
<script runat="server">
void Application_BeginRequest(object sender, System.EventArgs e) {
  Response.ContentType = "text/plain";
  Response.Write("Hello, World!");
  Context.ApplicationInstance.CompleteRequest();
}
</script>
