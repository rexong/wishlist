import { ColumnDef } from "@tanstack/react-table"

export const columns: ColumnDef<TWish>[] = [
    {
        accessorKey: "title",
        header: "Title"
    },
    {
        accessorKey: "description",
        header: "Description"
    },
    {
        accessorKey: "link",
        header: "Link"
    },
    {
        accessorKey: "is_hidden",
        header: "Hide"
    },
    {
        header: "Delete"
    }
]