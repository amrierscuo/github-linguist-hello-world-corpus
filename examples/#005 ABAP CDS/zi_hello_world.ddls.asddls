@EndUserText.label: 'Hello corpus greeting'
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity ZI_Hello_World
  as select from t000
{
  key mandt as Client,
      'Hello, World!' as Greeting
}
