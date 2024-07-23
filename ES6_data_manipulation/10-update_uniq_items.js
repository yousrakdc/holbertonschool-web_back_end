/* eslint-disable */
export default function updateUniqueItems(groceries) {
    if (!(groceries instanceof Map)) {
        throw new Error('Cannot process');
    }

    for (const [item, quantity] of groceries.entries()) {
        if (quantity === 1) {
            groceries.set(item, 100)
        }
    }

    return groceries;
}