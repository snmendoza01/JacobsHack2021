import "./css/App.css";
import { useState } from "react";

import { AnimatePresence, motion } from "framer-motion";
import { ThemeToggle } from "./components/dark";
import { BubbleBubbleToggleSVG } from "./components/img/svg";

import HomePage from "./components/HomePage/homePage";
import Footer from "./components/footer";
import Header from "./components/header";

function App() {
    const [showBubles, setShowBubbles] = useState(true);
    const [showFooter, setShowFooter] = useState(true);
    return (
        <div className="bg-gradient-to-t from-blue-900 via-blue-600 to-blue-400 dark:from-blue-900 dark:via-blue-800 dark:to-blue-400">
            <AnimatePresence>
                {/* header */}
                <Header key="header" />

                <motion.div
                    initial={{ opacity: 0 }}
                    animate={{ opacity: 1 }}
                    exit={{ opacity: 0 }}
                    transition={{ duration: 1 }}
                    className="flex justify-end my-2 mr-2"
                    key="motion"
                >
                    <ThemeToggle key="themeToggle" />
                </motion.div>
                <div className="flex justify-end mr-2" key="bubbleToggleDiv">
                    <BubbleBubbleToggleSVG
                        key="bubblesToggle"
                        setShowBubbles={setShowBubbles}
                        showBubles={showBubles}
                    />
                </div>
                <HomePage key="homepage" showBubles={showBubles} />

                {showFooter ? (
                    <Footer
                        key="footer"
                        setShowFooter={setShowFooter}
                        showFooter={showFooter}
                    />
                ) : (
                    <></>
                )}
            </AnimatePresence>
        </div>
    );
}

export default App;
