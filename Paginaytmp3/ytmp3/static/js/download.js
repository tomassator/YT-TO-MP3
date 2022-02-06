

function showContent() {
        divmp3 = document.getElementById("dropmp3");
        divmp4 = document.getElementById("dropmp4");
        divvid = document.getElementById("dropvid");
        spanInput = document.getElementById("spanInput")
        btn = document.getElementById("btnDescarga")

        checkmp3 =  document.getElementById("btnmp3");
        checkmp4 =  document.getElementById("btnmp4");
        checkvid =  document.getElementById("btnvid");

        spanInput.style.display='block';
        btnDescarga.style.display='block';


        if (checkmp3.checked) {
            divmp3.style.display='flex';
        }
        else {
            divmp3.style.display='none';
        }
        if (checkmp4.checked) {
            divmp4.style.display='flex';
        }
        else {
            divmp4.style.display='none';
        }
        if (checkvid.checked) {
            divvid.style.display='flex';
        }
        else {
            divvid.style.display='none';
        }

    }