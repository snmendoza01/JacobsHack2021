import { motion } from "framer-motion";
import { useState } from "react";

import SearchBar from "./searchBar";
import DisplayPrimaryInfo from "./displayInfo";
import { PredictSongsPOST } from "../connections";
import { Bubble } from "../img/svg";

export default function HomePage() {
    const [searchValue, setSearchValue] = useState("");
    const [returnedValue, setReturnedValue] = useState([]);
    const [ids, setIDs] = useState([]);

    const array = Array(20).fill(true);

    return (
        <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
        >
            <div className="flex min-h-screen subpixel-antialiased">
                <div className="relative w-11/12 m-auto">
                    <div className="px-2 pt-5 pb-2 mb-32 bg-gray-200 rounded-lg shadow-xl dark:bg-gray-700 dark:ring-2 dark:ring-gray-500 ring-opacity-80">
                        <SearchBar
                            searchValue={searchValue}
                            setSearchValue={setSearchValue}
                            setReturnedValue={setReturnedValue}
                        />
                    </div>

                    {array.map((element, index) => {
                        const size = Math.floor(Math.random() * 9) + 4;
                        return (
                            <Bubble key={index} width={size} height={size} />
                        );
                    })}

                    <div className="space-y-2">
                        <DisplayPrimaryInfo
                            returnedValue={returnedValue}
                            setIDs={setIDs}
                            ids={ids}
                        />
                        <div className="flex justify-center">
                            <button
                                className="w-1/3 px-1 text-gray-200 bg-green-500 rounded-md"
                                onClick={() => {
                                    PredictSongsPOST(ids);
                                    console.log(ids);
                                }}
                            >
                                Go
                            </button>
                        </div>
                    </div>
                </div>
            </div>

            <div className="flex max-h-full min-h-screen subpixel-antialiased bg-green-500"></div>
        </motion.div>
    );
}
