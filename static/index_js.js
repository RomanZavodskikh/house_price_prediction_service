function onInfoClick() {
    var info = document.querySelector("#project-info");
    var contacts = document.querySelector("#contacts");
    var info_button = document.querySelector("#info-button");
    var contacts_button = document.querySelector("#contacts-button");     

    info.classList.remove('hidden');
    contacts.classList.add('hidden');
    
    info_button.classList.add('active');
    contacts_button.classList.remove('active');    

}

function onContactsClick() {
    var info = document.querySelector("#project-info");
    var contacts = document.querySelector("#contacts");
    var info_button = document.querySelector("#info-button"); 
    var contacts_button = document.querySelector("#contacts-button");
    
    info.classList.add('hidden');
    contacts.classList.remove('hidden');
    
    info_button.classList.remove('active');
    contacts_button.classList.add('active');
}
