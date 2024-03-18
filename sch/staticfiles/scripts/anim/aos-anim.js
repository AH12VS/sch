function fdup() {
    var fdups = document.querySelectorAll(".fdup");

    for (var i = 0; i < fdups.length; i++) {
        var windowHeight = window.innerHeight;
        var elementTop = fdups[i].getBoundingClientRect().top;
        var elementVisible = 10;

        if (elementTop < windowHeight - elementVisible) {
            if (document.getElementById("scroll-hint-div")) {
                var var1 = document.getElementById("scroll-hint-div");
                var1.style.display = "none";
            }
            fdups[i].classList.add("active");
        } else {
            fdups[i].classList.remove("active");
        }
    }
}

// function fddwn() {
//     var fddwns = document.querySelectorAll(".fddwn");

//     for (var i = 0; i < fddwns.length; i++) {
//         var windowHeight = window.innerHeight;
//         var elementTop = fddwns[i].getBoundingClientRect().top;
//         var elementVisible = 50;

//         if (elementTop < windowHeight - elementVisible) {
//             if (document.getElementById("scroll-hint-div")) {
//                 var var1 = document.getElementById("scroll-hint-div");
//                 var1.style.display = "none";
//             }
//             fddwns[i].classList.add("active");
//         } else {
//             fddwns[i].classList.remove("active");
//         }
//     }
// }

// function fdrgt() {
//     var fdrgts = document.querySelectorAll(".fdrgt");

//     for (var i = 0; i < fdrgts.length; i++) {
//         var windowHeight = window.innerHeight;
//         var elementTop = fdrgts[i].getBoundingClientRect().top;
//         var elementVisible = 50;

//         if (elementTop < windowHeight - elementVisible) {
//             if (document.getElementById("scroll-hint-div")) {
//                 var var1 = document.getElementById("scroll-hint-div");
//                 var1.style.display = "none";
//             }
//             fdrgts[i].classList.add("active");
//         } else {
//             fdrgts[i].classList.remove("active");
//         }
//     }
// }

// function fdlft() {
//     var fdlfts = document.querySelectorAll(".fdlft");

//     for (var i = 0; i < fdlfts.length; i++) {
//         var windowHeight = window.innerHeight;
//         var elementTop = fdlfts[i].getBoundingClientRect().top;
//         var elementVisible = 50;

//         if (elementTop < windowHeight - elementVisible) {
//             if (document.getElementById("scroll-hint-div")) {
//                 var var1 = document.getElementById("scroll-hint-div");
//                 var1.style.display = "none";
//             }
//             fdlfts[i].classList.add("active");
//         } else {
//             fdlfts[i].classList.remove("active");
//         }
//     }
// }


window.addEventListener("scroll", fdup);
// window.addEventListener("scroll", fddwn);
// window.addEventListener("scroll", fdrgt);
// window.addEventListener("scroll", fdlft);
