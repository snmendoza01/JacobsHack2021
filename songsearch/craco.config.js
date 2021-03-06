// craco.config.js

const InlineChunkHtmlPlugin = require("react-dev-utils/InlineChunkHtmlPlugin");

module.exports = {
    // tailwindcss
    style: {
        postcss: {
            plugins: [require("tailwindcss"), require("autoprefixer")],
        },
    },

    // build all into one html file (https://pangyiwei.medium.com/building-a-react-app-as-a-single-html-file-with-create-react-app-no-eject-283a141e7635)
    webpack: {
        configure: (webpackConfig, { env, paths }) => {
            webpackConfig.plugins.forEach((plugin) => {
                if (plugin instanceof InlineChunkHtmlPlugin) {
                    plugin.tests = [/.+[.]js/];
                }
            });

            const oneOfRuleIdx = webpackConfig.module.rules.findIndex(
                (rule) => !!rule.oneOf
            );
            webpackConfig.module.rules[oneOfRuleIdx].oneOf.forEach((loader) => {
                if (
                    loader.test &&
                    loader.test.test &&
                    (loader.test.test("test.module.css") ||
                        loader.test.test("test.module.scss"))
                ) {
                    loader.use.forEach((use) => {
                        if (
                            use.loader &&
                            use.loader.includes("mini-css-extract-plugin")
                        ) {
                            use.loader = require.resolve("style-loader");
                        }
                    });
                }
            });
            return webpackConfig;
        },
    },
};
