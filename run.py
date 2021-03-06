from flask import Flask, render_template
app = Flask(__name__)

laBase = {'tel' :'Tel Entreprise', 'mail': 'Mail Entreprise', 
'rub1' : 'rubrique1', 'rub2': 'rubrique2', 'rub3':'rubrique3', 'rub4':'rubrique4', 'rub5':'rubrique5', 'rub6':'rubrique6',
 'nomEntreprise':"nom de l'entreprise", 'image':'LogoSidonieMenu.png'
 }

lesmarques = { 'titre1': 'Titre', 'titre2': 'Titre', 'titre3': 'Titre', 'titre4': 'Titre', 'titre5': 'Titre','titre6': 'Titre', 'titre7': 'Titre',
'soustitre1':'Sous-Titre','soustitre2': 'Sous-Titre','soustitre3': 'Sous-Titre','soustitre4': 'Sous-Titre','soustitre5': 'Sous-Titre','soustitre6': 'Sous-Titre',
'soustitre7': 'Sous-Titre','soustitre8':'Sous-Titre',
'texte1': 'Texte', 'texte2': 'Texte', 'texte3': 'Texte', 'texte4': 'Texte', 'texte5': 'Texte','texte6': 'Texte', 'texte7': 'Texte','texte8':'Texte',
'image1' : 'atelierdelice.jpg', 'image2' : 'atelierdelice.jpg', 'image3' : 'atelierdelice.jpg', 'image4' : 'atelierdelice.jpg',
'image5' : 'atelierdelice.jpg', 'image6' : 'atelierdelice.jpg', 'image7' : 'atelierdelice.jpg', 'image8' : 'atelierdelice.jpg'
}

lecontact = { 'nomsite': 'Le nom de votre site', 'rue': "La rue de l'entreprise", 'ville': "La ville de l'entreprise"
}

leaccueil = { 'nomEntreprise' : "Votre nom", 'metier': "Votre métier", 'titre1': 'titre1', 'titre2': 'titre2', 'titre3': 'titre3', 
'titre4': 'titre4', 'lien1' : "Lien 1", 'lien2' : "Lien 2", 'lien3' : "Lien 3", 'lien4' : "Lien 4", 'texte' : 'Votre texte', 
'article1' : "Un article",  'article2' : "Un article",  'article3' : "Un article",  'article4' : "Un article",  
'article5' : "Un article",
'article6' : "Un article", 'article7' : "Un article", 'article8' : "Un article", 'article9' : "Un article",
'image1': "LogoSidonie.png",'image2': "pinceau.jpg",'image3': "yeux.png",'image4': "1.png",'image5': "2.png",
'image6': "3.png",'image7': "4.png",'image8': "5.png",'image9': "6.png",'image10': "1.jpg",'image11': "2.jpg",'image12': "3.jpg",
}
 
lesprestations = { 'titre1': 'Titre', 'titre2': 'Titre', 'titre3': 'Titre',
'soustitre1':'Sous-Titre','soustitre2': 'Sous-Titre','soustitre3': 'Sous-Titre','soustitre4': 'Sous-Titre','soustitre5': 'Sous-Titre','soustitre6': 'Sous-Titre',
'soustitre7': 'Sous-Titre','soustitre8':'Sous-Titre',
'texte1': 'Texte', 'texte2': 'Texte', 'texte3': 'Texte', 'texte4': 'Texte', 'texte5': 'Texte','texte6': 'Texte', 'texte7': 'Texte','texte8':'Texte',
'texte9' : 'Texte', 'texte10' : 'Texte',
'image1': "1.jpg",'image2': "2.jpg",'image3': "3.jpg",'image4': "4.png",'image5': "5.png",
'image6': "6.png",'image7': "7.png",'image8': "8.png",'image9': "9.png",'image10': "10.jpg",'image11': "11.jpg",'image12': "12.jpg",
'image13': "13.png",'image14': "14.png",'image15': "15.png",'image16': "16.png"
}

leinstitut = { "titre1":"Titre","img1":'1.png',"img2":'2.png',"texte1":"Texte","texte2":"Texte",
"texte3":"Texte","texte4":"Texte","titre2":"Titre","img3":"3.png","img4":"4.png","img5":"5.png","img6":"6.png", "fond" : "fond.jpg"}


tarifs = {  "titre1":"titre page","titre2":"titre2","texte1":"texte","texte2":"texte",
"texte3":"texte","bouton1":"bouton","img1":"1.jpg","img2":"2.jpg","img3":"3.jpg","texte7":"texte","texte8":"texte","texte9":"texte"
}

my_liste=[["Onglerie",[['Beauté des mains et des pieds',["Manucure…………………………………………………………………….22€",
"Spa des mains (manucure avec gommage,masque)……..35€",
"Soins paraffine ajouté à un soins……………………………………9€",
"Pose de vernis (couleur/french)……………………………………35€",
"Beauté des pieds………………………………………………………….29€",
"Spa des pieds………………………………………………………………48€",
"Vernis semi-permanent(mains ou pieds………………………27€",
"Dépose seule………………………………………………………………..9€",
"Soin Calluspeeling®……………………………………………………..49€"]],
                    ['Prothésie ongulaire',['Pose complète sur chablon………………………………………..59€',
"Remplissage (4 semaines max)………………………………….47€",
"Gainage ongles naturels…………………………………………..47€",
"Ongles cassé……………………………………………………………..5€",
"Dépose + soin………………………………………………………….19€",
'Remplissage à 2 semaines………………………………………….32€']],
                    ['Décos',['Paillettes, pigments 10 ongles………………………………………..3€',
"Strass unité……………………………………………………………….0,50€",
'Peinture acrylique, aquarelle, gels peints à partir de………4€']]]],
        ["Beauté du regard",[['Regard',['Teinture des cils ou sourcils………………………………….16€',
'Rehaussement de cils………………………………………….44€']],
                    ['Maquillage miss W',['Maquillage jour…………………………………………………………….24€',
"Maquillage soir /cérémonie………………………………………….46€",
"Maquillage mariée avec essai……………………………………….68€"]]]],
        ["Maquilage Permanent",[['Lèvres',['Coutour…………………………………………………………….300€',
'Contour + voilage………………………………………….450€']],
                    ['Sourcils',["Ombrage…………………………………………………………….300€",
"Esquisse des poils………………………………………………300€",
"Ombrage + poil à poil……………………………………….500€"]],
                    ['Yeux',["Densification des cils hauts ………………………………………..200€",
"Densification haut + bas…………………………………………….250€",
"Eye liner………………………………………………………………Sur devis"]]]]]

@app.route("/")
def template_test():
    return render_template('Taccueil.html', base = laBase, marque = lesmarques, contact = lecontact, accueil = leaccueil, prestations = lesprestations)


@app.route("/rubrique1")
def accueil():
    return render_template('Taccueil.html', base = laBase, contact = lecontact, accueil = leaccueil)

@app.route("/rubrique2")
def linstitut():
    return render_template('Tinstitut.html', base = laBase, contact = lecontact, institut = leinstitut )

@app.route("/rubrique3")
def prestations():
    return render_template('Tprestations.html', base = laBase, contact = lecontact, prestations = lesprestations)

@app.route("/rubrique4")
def tarif():
    return render_template('Ttarifs.html', base = laBase,tarifs = tarifs, contact = lecontact, lestarifs = my_liste)


@app.route("/rubrique5")
def marque():
    return render_template('Tmarques.html', base = laBase, marque = lesmarques, contact = lecontact )

@app.route("/rubrique6")
def contact():
    return render_template('Tcontact.html', base = laBase, contact = lecontact)




if __name__ == '__main__':
    app.run(debug=True)
