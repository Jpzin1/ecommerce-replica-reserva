var url = new URL(document.URL);
var itens = document.getElementsByClassName("item-ordenar");

for (i = 0; i < itens.length; i++) {
    itens[i]
    url.searchParams.set("ordem", itens[i].name)
    itens[i].href = url.href;  
}
