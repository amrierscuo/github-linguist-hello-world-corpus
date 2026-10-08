# 0285 — HTML+Razor: `.razor`

Ruolo: Componente Razor Blazor con markup e campo C#, distinto dalla pagina MVC .cshtml.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: ASP.NET Core Razor con .NET SDK e applicazione host; versioni effettive da registrare. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
SDK .NET con Blazor: aggiungere Hello.razor a un progetto e renderizzare il componente
```

Risultato atteso: Elemento p con Hello, World!

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `Hello.razor`: `7e37c225ae71b2b827243c4ace306420be08d7990f782e0d3b8ed74167b9d343`

Fonti primarie:

- https://learn.microsoft.com/en-us/aspnet/core/blazor/components/
- https://learn.microsoft.com/en-us/aspnet/core/mvc/views/razor?view=aspnetcore-10.0
