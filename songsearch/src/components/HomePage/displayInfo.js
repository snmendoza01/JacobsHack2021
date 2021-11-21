import { motion } from "framer-motion";

export default function DisplayPrimaryInfo({ returnedValue, setIDs, ids }) {
    return (
        <table className="w-full p-1 m-auto bg-gray-100 table-fixed dark:bg-gray-200 rounded-xl">
            <thead>
                <tr className="bg-blue-300 dark:bg-blue-400">
                    <th className="w-5/12 border-b border-r border-gray-600 rounded-tl-lg">
                        Artist
                    </th>
                    <th className="w-6/12 m-auto border-b border-r border-gray-600">
                        Track
                    </th>
                    <th className="w-1/12 border-b border-r border-gray-600 rounded-tr-lg">
                        <svg
                            xmlns="http://www.w3.org/2000/svg"
                            className="block w-5 h-5 m-auto"
                            viewBox="0 0 20 20"
                            fill="currentColor"
                        >
                            <path d="M5 4a1 1 0 00-2 0v7.268a2 2 0 000 3.464V16a1 1 0 102 0v-1.268a2 2 0 000-3.464V4zM11 4a1 1 0 10-2 0v1.268a2 2 0 000 3.464V16a1 1 0 102 0V8.732a2 2 0 000-3.464V4zM16 3a1 1 0 011 1v7.268a2 2 0 010 3.464V16a1 1 0 11-2 0v-1.268a2 2 0 010-3.464V4a1 1 0 011-1z" />
                        </svg>
                    </th>
                </tr>
            </thead>
            <tbody className="">
                {Object.keys(returnedValue).map((elem, index) => {
                    return (
                        <tr
                            key={index}
                            className="bg-transparent dark:even:bg-gray-400 even:bg-gray-300"
                        >
                            <td className="h-full px-1 text-sm text-center truncate border-t border-r border-gray-600">
                                {JSON.stringify(
                                    returnedValue[elem].artist
                                ).replace(/(^"|"$)/g, "")}
                            </td>
                            <td className="px-1 text-sm text-center truncate border-t border-l border-gray-600">
                                {JSON.stringify(
                                    returnedValue[elem].track_name
                                ).replace(/(^"|"$)/g, "")}
                            </td>

                            <td className="border-t border-l border-gray-600 ">
                                {ids.includes(returnedValue[elem].track_id) ? (
                                    <motion.svg
                                        whileTap={{ scale: 0.9 }}
                                        xmlns="http://www.w3.org/2000/svg"
                                        className="block w-5 h-5 m-auto text-red-600 dark:text-red-700"
                                        fill="none"
                                        key="remove"
                                        viewBox="0 0 24 24"
                                        stroke="currentColor"
                                        onClick={() =>
                                            setIDs(
                                                ids.filter(
                                                    (oldVals) =>
                                                        oldVals !==
                                                        returnedValue[elem]
                                                            .track_id
                                                )
                                            )
                                        }
                                    >
                                        <path
                                            strokeLinecap="round"
                                            strokeLinejoin="round"
                                            strokeWidth={2}
                                            d="M6 18L18 6M6 6l12 12"
                                        />
                                    </motion.svg>
                                ) : (
                                    <motion.svg
                                        key="add"
                                        whileTap={{ scale: 0.9 }}
                                        xmlns="http://www.w3.org/2000/svg"
                                        className="block w-6 h-6 m-auto text-green-600 dark:text-green-600"
                                        fill="none"
                                        viewBox="0 0 24 24"
                                        stroke="currentColor"
                                        onClick={() =>
                                            setIDs((oldVals) => [
                                                ...oldVals,
                                                returnedValue[elem].track_id,
                                            ])
                                        }
                                    >
                                        <path
                                            strokeLinecap="round"
                                            strokeLinejoin="round"
                                            strokeWidth={2}
                                            d="M12 4v16m8-8H4"
                                        />
                                    </motion.svg>
                                )}
                            </td>
                        </tr>
                    );
                })}
            </tbody>
        </table>
    );
}
