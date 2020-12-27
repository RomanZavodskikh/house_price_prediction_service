function onInfoClick() {
    var info = document.querySelector("#project-info");
    var contacts = document.querySelector("#contacts");
    
    info.classList.remove('hidden');
    contacts.classList.add('hidden');
}

function onContactsClick() {
    var info = document.querySelector("#project-info");
    var contacts = document.querySelector("#contacts");
    
    info.classList.add('hidden');
    contacts.classList.remove('hidden');
}
