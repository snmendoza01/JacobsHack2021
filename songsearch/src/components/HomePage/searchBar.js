import { motion } from "framer-motion";

import { SearchSVG } from "../img/svg";
import { SongPOST } from "../connections";

export default function SearchBar({
    searchValue,
    setSearchValue,
    setReturnedValue,
}) {
    function inputHandler(newValue) {
        setSearchValue(newValue);
    }
    return (
        <div className="space-y-4 ">
            <p className="font-semibold text-center dark:text-gray-200">
                Input a search term. Once you receive results, you may choose
                songs that suit you and click "Go". The server will then attempt
                to find your best.
            </p>
            <div className="flex justify-center space-x-2">
                <SearchSVG />
                <input
                    type="text"
                    placeholder="Search song"
                    onChange={(e) => inputHandler(e.target.value)}
                    value={searchValue}
                    className="px-2 rounded-md"
                />
            </div>
            <div className="flex justify-center">
                <motion.button
                    whileTap={{ scale: 0.95 }}
                    type="submit"
                    className={
                        searchValue
                            ? " ring-offset-1 ring-1 ring-blue-400 w-3/4 px-4 text-center text-white bg-blue-500 rounded-md dark:bg-blue-400"
                            : " ring-blue-400 w-3/4 opacity-75 px-4 text-center text-white bg-blue-500 rounded-md dark:bg-blue-400"
                    }
                    onClick={() => SongPOST(searchValue, setReturnedValue)}
                >
                    Search
                </motion.button>
            </div>
        </div>
    );
}
