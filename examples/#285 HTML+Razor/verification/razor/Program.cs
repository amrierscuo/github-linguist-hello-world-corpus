using Microsoft.AspNetCore.Components;
using Microsoft.AspNetCore.Components.Web;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.DataProtection;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.Abstractions;
using Microsoft.AspNetCore.Mvc.ModelBinding;
using Microsoft.AspNetCore.Mvc.Rendering;
using Microsoft.AspNetCore.Mvc.ViewEngines;
using Microsoft.AspNetCore.Mvc.ViewFeatures;
using Microsoft.AspNetCore.Routing;
using RazorHarness;

var builder = WebApplication.CreateBuilder(args);
builder.Logging.ClearProviders();
builder.Services.AddDataProtection().UseEphemeralDataProtectionProvider();
builder.Services.AddControllersWithViews();
await using var app = builder.Build();
await using var scope = app.Services.CreateAsyncScope();
var provider = scope.ServiceProvider;
var httpContext = new DefaultHttpContext { RequestServices = provider };
var action = new ActionContext(httpContext, new Microsoft.AspNetCore.Routing.RouteData(), new ActionDescriptor());
var view = provider.GetRequiredService<ICompositeViewEngine>().GetView(null, "/Views/Home/Hello.cshtml", true);
if (!view.Success) throw new InvalidOperationException(string.Join(", ", view.SearchedLocations));
using var mvcWriter = new StringWriter();
await view.View.RenderAsync(new ViewContext(action, view.View, new ViewDataDictionary(new EmptyModelMetadataProvider(), action.ModelState),
    new TempDataDictionary(httpContext, provider.GetRequiredService<ITempDataProvider>()), mvcWriter, new HtmlHelperOptions()));
Console.WriteLine("cshtml:" + mvcWriter.ToString().Trim());
await using var renderer = new HtmlRenderer(provider, provider.GetRequiredService<ILoggerFactory>());
var component = await renderer.Dispatcher.InvokeAsync(async () => {
    var output = await renderer.RenderComponentAsync<Hello>(ParameterView.Empty);
    return output.ToHtmlString();
});
Console.WriteLine("razor:" + component.Trim());
