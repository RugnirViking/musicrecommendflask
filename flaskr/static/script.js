

document.addEventListener('DOMContentLoaded', function() {
    // GDP data
    var svgMapDataGPD = {
        data: {
          listeners: {
            name: 'Listeners',
            format: '{0} vibers',
            thousandSeparator: ',',
            thresholdMax: 500000,
            thresholdMin: 4
          },
          stations: {
            name: 'Stations',
            format: '{0} radio stations',
            thousandSeparator: ',',
            thresholdMax: 500000,
            thresholdMin: 4
          },
        },
        values: {
          AF: {listeners: 5, stations: 3, link: '/viewcountry/AF'},
          AL: {listeners: 3, stations: 2, link: '/viewcountry/AL'},
          JP: {listeners: 15, stations: 8, link: '/viewcountry/JP'},

          DK: {listeners: 18, stations: 6, link: '/viewcountry/DK'},
          GB: {listeners: 22, stations: 15, link: '/viewcountry/GB'},
          US: {listeners: 12, stations: 18, link: '/viewcountry/US'},
        }
    }

    new svgMap({
        targetElementID: 'svgMapExample',
        data: svgMapDataGPD,
        touchLink: true
    });
}, false);