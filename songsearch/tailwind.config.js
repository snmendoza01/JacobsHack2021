module.exports = {
    purge: ["./src/**/*.{js,jsx,ts,tsx}", "./public/index.html"],
    darkMode: "class", // or 'media' or 'class'
    theme: {
        extend: {
            textColor: {
                "yellow-250": "#fcdd6d",
                "yellow-325": "#fbce44",
            },
        },
    },
    variants: {
        extend: {
            opacity: ["dark"],
            invert: ["dark"],
            filter: ["dark"],
            ringWidth: ["dark"],
            fill: ["dark"],
            backgroundColor: ["even"],
        },
    },
    plugins: [],
};
