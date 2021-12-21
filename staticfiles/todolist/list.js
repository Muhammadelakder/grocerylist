
// اضافة ميزة مكاني الحالي
document.addEventListener('DOMContentLoaded', function(){

    // ارسال طلب عبر الويب (API)
    fetch("https://api.ipify.org/?format=json")
    .then(response => response.json())
    .then(ip => {
        console.log(ip)

        // ارسال طلب اخر للحصول علي معلومات عن (IP)
        fetch(`https://ipinfo.io/${ip.ip}/geo`)
        .then(response => response.json())
        .then(ipinfo => {
            console.log(ipinfo)

            info = document.createElement('div');
            info.innerHTML = `${ipinfo.city}`
            
            document.querySelector('#ip').addEventListener('click', function() {
                document.querySelector('#ipinfo').append(info)
            })
        })
    })

})