ymaps.ready(init);
var myMap;

function getCoords(x, y) {
    document.getElementById('id_latitude').value = x
    document.getElementById('id_longitude').value = y
}

function init() {
    myMap = new ymaps.Map("map", {
        center: [56.83507546894007, 60.59762278832995], // Екб
        zoom: 13
    }, {
        balloonMaxWidth: 200,
        searchControlProvider: 'yandex#search'
    });

    myMap.events.add('click', function (e) {
        if (!myMap.balloon.isOpen()) {
            var coords = e.get('coords')
            myMap.balloon.open(coords, {
                contentHeader: 'Great place in this city! :)',
                contentBody: '<p>What happened here?</p>',
                contentFooter: '<sup>Click again</sup>'
            });

            getCoords(coords[0], coords[1])
        } else {
            myMap.balloon.close();
        }
    });
}