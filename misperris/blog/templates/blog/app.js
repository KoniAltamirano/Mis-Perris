if ('serviceWorker' in navigator) {
    navigator.serviceWorker
        .register('static/Js/sw.js',{ scope : '/static/' })
        .then(function (registration) {
            console.log("Service Worker Registered", registration);
        })
        .catch(function (err) {
            console.log("service worker failed to registrer", err)

        })

}