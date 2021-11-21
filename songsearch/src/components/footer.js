import { motion } from "framer-motion";

export default function Footer({ showFooter, setShowFooter }) {
    return (
        <motion.div
            className="fixed inset-x-0 bottom-0 mx-2"
            drag="y"
            dragConstraints={{ top: 0, bottom: 300 }}
        >
            <div className="px-2 pt-1 pb-3 space-y-2 bg-gray-600 rounded-t-2xl ring-1 ring-gray-50 ">
                <p className="text-xl font-bold text-center text-gray-200">
                    Privacy Notice
                </p>
                <p className="text-lg text-center text-gray-300 ">
                    This if a formal privacy notice that your inputs will be
                    processed on a server within Germany as well as in any
                    nations in which the 3rd party services are provided.
                </p>
                <div className="flex justify-center">
                    <button
                        className="w-2/3 px-2 py-1 bg-gray-300 rounded-md shadow-xl ring-0 ring-offset-4 ring-offset-gray-800"
                        onClick={() => setShowFooter(!showFooter)}
                    >
                        Accept
                    </button>
                </div>
            </div>
        </motion.div>
    );
}
