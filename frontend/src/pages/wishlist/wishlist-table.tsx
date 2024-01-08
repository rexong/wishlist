import { Link as LinkIcon, Eye, EyeOff, Trash } from 'lucide-react'

import {
  ColumnDef,
  flexRender,
  getCoreRowModel,
  useReactTable,
  getPaginationRowModel,
  Cell
} from "@tanstack/react-table"

import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table"
import { Button } from "@/components/ui/button"
import { Link } from 'react-router-dom'
import { useState } from 'react'

interface DataTableProps<TData, TValue> {
  columns: ColumnDef<TData, TValue>[]
  data: TData[]
}

export function DataTable<TData, TValue>({
  columns,
  data,
}: DataTableProps<TData, TValue>) {
  const [currentPageNumber, setCurrentPageNumber] = useState(1)
  const table = useReactTable({
    data,
    columns,
    getCoreRowModel: getCoreRowModel(),
    getPaginationRowModel: getPaginationRowModel(),
  })

  function renderCell(cell: Cell<TData, unknown>, i: number) {
    if (i === 0) {
      return <b>{flexRender(cell.column.columnDef.cell, cell.getContext())}</b>
    }
    if (i === 1) {
      return flexRender(cell.column.columnDef.cell, cell.getContext())
    }
    if (i === 2) {
      return renderLinkIcon(cell.renderValue() as string)
    }
    if (i === 3) {
      const isHidden = cell.renderValue() as boolean
      return isHidden ? <EyeOff /> : <Eye />
    }
    if (i === 4) {
      return <Trash />
    }
  }

  function renderLinkIcon(link: string) {
    if (!link) {
        return null
    }

    return (
      <Link to={link}>
         <LinkIcon />
      </Link>
    )
  }

  return (
    <div>
      <div className="rounded-md border">
        <Table>
          <TableHeader>
            {table.getHeaderGroups().map((headerGroup) => (
              <TableRow key={headerGroup.id}>
                {headerGroup.headers.map((header) => {
                  return (
                    <TableHead key={header.id} className="text-lg">
                      {header.isPlaceholder
                        ? null
                        : flexRender(
                            header.column.columnDef.header,
                            header.getContext()
                          )}
                    </TableHead>
                  )
                })}
              </TableRow>
            ))}
          </TableHeader>
          <TableBody>
            {table.getRowModel().rows?.length ? (
              table.getRowModel().rows.map((row) => (
                <TableRow
                  key={row.id}
                  data-state={row.getIsSelected() && "selected"}
                >
                  {row.getVisibleCells().map((cell, i) => (
                    <TableCell className="text-lg" key={cell.id}>
                      {renderCell(cell, i)}
                    </TableCell>
                  ))}
                </TableRow>
              ))
            ) : (
              <TableRow>
                <TableCell colSpan={columns.length} className="h-24 text-center text-lg">
                  No results.
                </TableCell>
              </TableRow>
            )}
          </TableBody>
        </Table>
      </div>
      <div className="flex items-center justify-end space-x-2 py-4">
        <Button
          variant="outline"
          size="sm"
          onClick={() => {
            table.previousPage()
            setCurrentPageNumber(prev => prev - 1)
          }}
          disabled={!table.getCanPreviousPage()}
        >
          Previous
        </Button>
        <span>{currentPageNumber}</span>
        <Button
          variant="outline"
          size="sm"
          onClick={() => {
            table.nextPage()
            setCurrentPageNumber(prev => prev + 1)
          }}
          disabled={!table.getCanNextPage()}
        >
          Next
        </Button>
      </div>
    </div>
  )
}
