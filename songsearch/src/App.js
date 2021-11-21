import "./css/App.css";

import { Route, Routes, BrowserRouter } from "react-router-dom";
import { AnimatePresence, motion } from "framer-motion";
import { ThemeToggle } from "./components/dark";

import HomePage from "./components/HomePage/homePage";
import Footer from "./components/footer";
import Header from "./components/header";

function App() {
    return (
        <BrowserRouter>
            <div className="bg-gradient-to-t from-blue-900 via-blue-600 to-blue-400 dark:from-blue-900 dark:via-blue-800 dark:to-blue-400">
                <AnimatePresence exitBeforeEnter>
                    {/* header */}
                    <Header key="header" />
                    <motion.div
                        initial={{ opacity: 0 }}
                        animate={{ opacity: 1 }}
                        exit={{ opacity: 0 }}
                        transition={{ duration: 1 }}
                        className="flex justify-end my-2 mr-2"
                        key="themeToggle"
                    >
                        <ThemeToggle />
                    </motion.div>

                    <Routes>
                        <Route
                            exact
                            path="/"
                            key="home"
                            element={<HomePage />}
                        />
                    </Routes>
                    <Footer key="footer" />
                </AnimatePresence>
            </div>
        </BrowserRouter>
    );
}

export default App;
