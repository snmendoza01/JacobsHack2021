import { motion } from "framer-motion";
import { useState } from "react";

import { SubmitRating } from "../connections";

export default function RatingComponent() {
    const [sliderValue, setSliderValue] = useState(50);

    return (
        <motion.div className="px-2 pt-5 pb-2 mt-5 mb-10 bg-gray-300 rounded-lg shadow-xl ring-2 ring-gray-500 dark:bg-gray-700 dark:ring-gray-500 ring-opacity-80">
            <p className="text-center text-gray-600 dark:text-gray-100">
                What did you think of the recommendation?
            </p>
            <div className="grid grid-cols-3 mt-3">
                <p className="col-span-1 text-gray-600 dark:text-gray-100 justify-self-start ">
                    0
                </p>
                <p className="col-span-1 text-gray-600 dark:text-gray-100 justify-self-center ">
                    50
                </p>
                <p className="col-span-1 text-gray-600 dark:text-gray-100 justify-self-end ">
                    100
                </p>
            </div>

            <input
                type="range"
                min="0"
                max="100"
                onChange={(e) => setSliderValue(e.target.value)}
                value={sliderValue}
                className="w-full"
            />
            <div className="flex justify-center ">
                <button
                    className="w-2/3 px-2 py-1 text-gray-100 bg-blue-400 rounded-lg"
                    onClick={() => SubmitRating(sliderValue)}
                >
                    Submit
                </button>
            </div>
        </motion.div>
    );
}
