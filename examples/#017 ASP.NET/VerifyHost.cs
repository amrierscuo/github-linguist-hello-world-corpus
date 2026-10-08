using System;
using System.IO;
using System.Threading;
using System.Web;
using System.Web.Hosting;

public sealed class GreetingHost : MarshalByRefObject
{
    public string Render()
    {
        using (StringWriter output = new StringWriter())
        using (ManualResetEvent finished = new ManualResetEvent(false))
        {
            HttpRuntime.ProcessRequest(new GreetingRequest(output, finished));
            if (!finished.WaitOne(TimeSpan.FromSeconds(30)))
                throw new TimeoutException("ASP.NET response did not finish.");
            return output.ToString();
        }
    }
}

public sealed class GreetingRequest : SimpleWorkerRequest
{
    private readonly ManualResetEvent finished;

    public GreetingRequest(TextWriter output, ManualResetEvent finished)
        : base("hello.aspx", "", output)
    {
        this.finished = finished;
    }

    public override void EndOfRequest()
    {
        base.EndOfRequest();
        finished.Set();
    }
}

public static class VerifyHost
{
    public static int Main(string[] args)
    {
        try
        {
            GreetingHost host = (GreetingHost)ApplicationHost.CreateApplicationHost(
                typeof(GreetingHost), "/", Path.GetFullPath(args[0]));
            string rendered = host.Render().Trim();
            if (rendered != "Hello World")
            {
                Console.Error.WriteLine("FAIL: unexpected ASP.NET response");
                Console.Error.WriteLine(rendered);
                return 1;
            }
            Console.WriteLine("CLR: " + Environment.Version);
            Console.WriteLine("System.Web: " + typeof(HttpRuntime).Assembly.GetName().Version);
            Console.WriteLine("Rendered: " + rendered);
            Console.WriteLine("PASS: ASP.NET compiled and executed hello.aspx");
            return 0;
        }
        catch (Exception error)
        {
            Console.Error.WriteLine(error.GetType().Name + ": " + error.Message);
            return 1;
        }
    }
}
