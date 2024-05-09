// Gestion de la coloration du background
document.addEventListener('DOMContentLoaded', function() {
    let body = document.getElementById('bodyID');
    let color = document.getElementById('colorIN');
    if (color != null)
    {
        let colorsaved = localStorage.getItem('selectedColor');
        if (colorsaved){
           color.value = colorsaved
           body.style.backgroundColor = color.value;
        }
            color.addEventListener('input', function(){
            body.style.backgroundColor = color.value;
            let colorsaved = localStorage.setItem('selectedColor', color.value);
        });
    }
})


function italiqueON() {
    // Permet de mettre les balises pour mettre en italique, un texte sélectionné
    var textarea = document.getElementById("text");
    var selec = textarea.value.substring(textarea.selectionStart, textarea.selectionEnd);
    textarea.setRangeText("<i>" + selec + "</i>", textarea.selectionStart, textarea.selectionEnd, "end");
}

function ligneON() {
    // Permet de mettre les balises pour souligner, un texte sélectionné
    var textarea = document.getElementById("text");
    var selec = textarea.value.substring(textarea.selectionStart, textarea.selectionEnd);
    textarea.setRangeText("<u>" + selec + "</u>", textarea.selectionStart, textarea.selectionEnd, "end");
}

function grasON() {
    // Permet de mettre les balises pour mettre en gras, un texte sélectionné
    var textarea = document.getElementById("text");
    var selec = textarea.value.substring(textarea.selectionStart, textarea.selectionEnd);
    textarea.setRangeText("<b>" + selec + "</b>", textarea.selectionStart, textarea.selectionEnd, "end");
}

function colorON() {
    // Permet de mettre les balises pour mettre en une certaine couleur, un texte sélectionné
    var textarea = document.getElementById("text");
    var couleur = document.getElementById('colorTXT').value;
    var selec = textarea.value.substring(textarea.selectionStart, textarea.selectionEnd);
    textarea.setRangeText("<span style='color:" + couleur + "'>" + selec + "</span>", textarea.selectionStart, textarea.selectionEnd, "end");
}

function titleON() {
    // Permet de mettre les balises pour mettre un titre (ici h2), un texte sélectionné
    var textarea = document.getElementById("text");
    var selec = textarea.value.substring(textarea.selectionStart, textarea.selectionEnd);
    textarea.setRangeText("<h2>" + selec + "</h2>", textarea.selectionStart, textarea.selectionEnd, "end");
}

function subtitleON() {
    // Permet de mettre les balises pour mettre un sous-titre (ici h3), un texte sélectionné
    var textarea = document.getElementById("text");
    var selec = textarea.value.substring(textarea.selectionStart, textarea.selectionEnd);
    textarea.setRangeText("<h3>" + selec + "</h3>", textarea.selectionStart, textarea.selectionEnd, "end");
}
