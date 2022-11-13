

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
          BR: {listeners: 11, stations: 18, link: '/viewcountry/BR'},

          DE: {listeners: 6, stations: 6, link: '/viewcountry/DE'},
          ID: {listeners: 9, stations: 3, link: '/viewcountry/ID'},
          RS: {listeners: 4, stations: 7, link: '/viewcountry/RS'},
          CN: {listeners: 44, stations: 36, link: '/viewcountry/CN'},
          IN: {listeners: 32, stations: 37, link: '/viewcountry/IN'},
        }
    }

    new svgMap({
        targetElementID: 'svgMapExample',
        data: svgMapDataGPD,
        touchLink: true
    });
}, false);