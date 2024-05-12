/**
 * @typedef {{ event?: string, callback: () => any}} ElementInitializerOption
 */

/**
 * Initialize all alpine components on document.
 * 
 * @exports
 * @param {ElementInitializerOption[]} componentsInits 
 */
function initAlpineElements(componentsInits) {
    componentsInits.forEach((e) => {
        if(!e.event) e.event = 'DOMContentLoaded';
        document.addEventListener(e.event, e.callback);
    });
}

