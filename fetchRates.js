function getCurrencyCode(iOptionElement)
{
    optionText = $(iOptionElement).text()
    console.assert(optionText.length > 3)
    return optionText.substring(0,3)
}

function getCurrencyName(iOptionElement)
{
    kSeparator = '-'
    optionText = $(iOptionElement).text()
    separatorIndex = optionText.indexOf(kSeparator)
    console.assert(separatorIndex != -1)
    return optionText.substring(separatorIndex + kSeparator.length).trim()
}

function isCurrencyAlreadyProcessed(iCurrencyCode, iCurrencyArray)
{
    if (iCurrencyArray.indexOf(iCurrencyCode) == -1)
    {
        iCurrencyArray.push(iCurrencyCode);
        return false;
    }
    else
    {
        return true;
    }
}

function isCurrencyToSkip(iOptionElement)
{
    if ($(iOptionElement).text() == "Select a Currency")
        return true;
    var currencyCodesToSkip = ["ADP", "ATS", "BEF", "CNH", "CYP", "DEM", "EEK", "ESP", "FIM", "FRF",
        "GRD", "IEP", "ITL", "LTL", "LUF", "LVL", "MTL", "NLG", "PTE", "SIT", "SKK", "TRL"];
    return currencyCodesToSkip.indexOf(getCurrencyCode(iOptionElement)) >= 0;
}

function printCurrencyCodeAndName()
{
    $("select[name='from_tkc'] option").each(function()
    {
        console.log(getCurrencyCode($(this)) + " " + getCurrencyName($(this)))
    });
}

function printExchangeRates()
{
    convertButton = $(".convert_btn")
    processedFrom = []

    $("select[name='from_tkc'] option").each(function()
    {
        if (isCurrencyToSkip($(this))
            return 0;

        fromCurrencyCode = getCurrencyCode($(this))
        if (!isCurrencyAlreadyProcessed(fromCurrencyCode, processedFrom))
        {
            $(this).attr('selected', 'selected');
            processedTo = []    
            $("select[name='to_tkc'] option").each(function()
            {
                if (isCurrencyToSkip($(this))
                    return 0;
                toCurrencyCode = getCurrencyCode($(this))
                if (!isCurrencyAlreadyProcessed(toCurrencyCode, processedTo))
                {
                    $(this).attr('selected', 'selected');
                    $(convertButton).trigger('click');
                    console.log(fromCurrencyCode + " " + toCurrencyCode + " " + $(".exchange_rate").text())
                }
            });
        }
    });
}

function exchangeRatesManager()
{
    printCurrencyCodeAndName();
    printExchangeRates();
}