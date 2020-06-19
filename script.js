let jours_a_remonter = [0, 3, 5, 8, 13, 21]
let jours_noms = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
let jours_noms_FR = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']

let emploi_du_temps = [
    {'Lundi': ['histoire', 'français']},
    {'Mardi': ['maths']},
    {'Mercredi': ['histoire']},
    {'Jeudi': ['maths', 'français']},
    {'Vendredi': ['histoire', 'maths', 'français']},
    {'Samedi': []},
    {'Dimanche': []}
]
let aujourdhui = new Date()
afficherSurLaPage(jours_noms_FR[aujourdhui.getDay()] + " " + aujourdhui.getDate().toString() + "/" + aujourdhui.getMonth(), 'div', 'h1')
for (let i = 0; i < jours_a_remonter.length; i++) {
    const nb = jours_a_remonter[i];
    let jour_a_reviser = new Date(aujourdhui - nb*3600*24*1000)

    let index_du_jour_a_reviser = jour_a_reviser.getDay()-1
    index_du_jour_a_reviser < 0 ? index_du_jour_a_reviser = 0 : null
    let nom_du_jour = jours_noms_FR[index_du_jour_a_reviser]
    console.log(jour_a_reviser.getDay())

    let matieres = emploi_du_temps[index_du_jour_a_reviser][nom_du_jour]
    if (matieres.length == 0)
        continue

    matieres_txt = ""
    for (let m = 0; m < matieres.length; m++) {
        const matiere = matieres[m];
        matieres_txt += matiere + " "
    }

    afficherSurLaPage(nom_du_jour+ " " + jour_a_reviser.getDate().toString() + "/" + jour_a_reviser.getMonth(), 'div', 'div1')
    afficherSurLaPage(matieres_txt, 'div', 'div1')
    afficherSurLaPage("", 'div', 'div1')
}

// Function pour ajouter du texte sur la page HTML liée
function afficherSurLaPage(txt, type, id) {
    // crée un nouvel élément div
    let newDiv = document.createElement(type);
    // et lui donne un peu de contenu
    let newContent = document.createTextNode(txt);
    // ajoute le nœud texte au nouveau div créé
    newDiv.appendChild(newContent);
    
    let currentDiv = document.querySelector("#" + id);
    // document.body.insertBefore(newDiv, currentDiv);
    currentDiv.appendChild(newDiv)
}
