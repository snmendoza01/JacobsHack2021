import { motion } from "framer-motion";

export default function FinalSong({ responceSongs }) {
    return (
        <motion.div
            className="px-2 pt-5 pb-2 mt-5 mb-10 bg-gray-300 rounded-lg shadow-xl ring-2 ring-gray-500 dark:bg-gray-700 dark:ring-gray-500 ring-opacity-80"
            animate={{ opacity: 1 }}
            initial={{ opacity: 0 }}
        >
            <p className="font-bold text-center dark:text-gray-100">
                The closest match was...
            </p>
            <p className="font-semibold text-center text-yellow-300 dark:text-yellow-500">
                {JSON.stringify(responceSongs)}
            </p>
        </motion.div>
    );
}
