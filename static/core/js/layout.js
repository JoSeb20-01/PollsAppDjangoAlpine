/**
 * TYPE DEFINITIONS - COMPONENTS
 * 
 * @typedef Layout
 * @prop {boolean} showSidebar
 * @prop {() => void} toggle
 * 
 * @typedef Sidebar
 * @prop {string} sectionSelected
 * @prop {(name) => boolean} isSelected
 * 
 * @typedef ItemSidebar
 * @prop {HTMLSpanElement} span
 * 
 */

/**
 * @returns {import("alpinejs").AlpineComponent<Layout>}
 */
const layout = function() {
    return {
        showSidebar: true,
        toggle(){
            this.showSidebar = !this.showSidebar;
        }
    }
}

/**
 * @returns {import("alpinejs").AlpineComponent<Sidebar & Layout>}
 */
const sidebar = function() {
    return {
        sectionSelected: Alpine.$persist('').using(sessionStorage),
        isSelected(name){
            return this.sectionSelected === name;
        }
    }
}

/**
 * 
 * @returns {import("alpinejs").AlpineComponent<Sidebar & Layout & ItemSidebar>}
 */
const itemSidebar = () => ({
    span: undefined,

    init(){
        this.span = this.$refs.spanElment;
    },

    bind(){
        return {
            'x-on:button': () => {
                this.sectionSelected = this.span.textContent;
            },
            'x-bind:class': () => ({
                'selected': this.isSelected(this.span.textContent)
            })
        }
    }
});

/**
 * Init Components
 */
initAlpineElements([
    { 
        event: 'alpine:initializing', 
        callback: () => {
            window.sidebar = sidebar();
            Alpine.data('itemSidebar', () => itemSidebar());
        }
    },
    {
        callback: () => {
            window.layout = layout();
        }
    },
]);
