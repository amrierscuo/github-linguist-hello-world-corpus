page 50100 "Corpus Hello"
{
    PageType = Card;
    ApplicationArea = All;
    UsageCategory = Tasks;
    Caption = 'Corpus Hello';

    trigger OnOpenPage()
    begin
        Codeunit.Run(Codeunit::"Corpus Hello");
    end;
}
