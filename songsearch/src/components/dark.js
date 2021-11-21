import { useEffect, useState } from "react";
import { motion } from "framer-motion";

import { SunSVG, MoonSVG, ArrowLeftSVG, ArrowRightSVG } from "./img/svg";

// control & hold dark/light info
export default function DarkModeComp() {
    const [theme, setTheme] = useState(localStorage.theme);
    const colorTheme = theme === "dark" ? "light" : "dark";

    useEffect(() => {
        const root = window.document.documentElement;
        root.classList.remove(colorTheme);
        root.classList.add(theme);
        localStorage.setItem("theme", theme);
    }, [theme, colorTheme]);

    return [colorTheme, setTheme];
}

// theme toggle
export function ThemeToggle() {
    const [colorTheme, setTheme] = DarkModeComp();

    const variants = {
        light: {
            x: -1.5,
            transition: {
                rotate: { duration: 0.5 },
            },
        },

        dark: {
            x: 40,

            transition: {
                rotate: { duration: 0.5 },
            },
        },
    };

    return (
        <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }}>
            <div className="flex items-center px-1 py-1 rounded-full shadow-sm bg-gradient-to-r from-yellow-200 via-yellow-400 to-blue-600 dark:bg-gradient-to-l dark:from-yellow-600 dark:via-blue-600 dark:to-blue-700 ring-2 ring-gray-400 w-min dark:ring-gray-700 ">
                <motion.div
                    className="absolute"
                    onClick={() => setTheme(colorTheme)}
                    animate={colorTheme === "light" ? "light" : "dark"}
                    variants={variants}
                    initial={{ x: 0 }}
                >
                    {colorTheme === "light" ? (
                        <ArrowLeftSVG />
                    ) : (
                        <ArrowRightSVG />
                    )}
                </motion.div>

                <div className="flex space-x-3.5 w-max">
                    {/* Light */}
                    <SunSVG />
                    {/* Moon */}
                    <MoonSVG />
                </div>
            </div>
        </motion.div>
    );
}
