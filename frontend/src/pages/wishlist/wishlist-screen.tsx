import getWishes from "@/mock_wishes"
import { DataTable } from "./wishlist-table"
import { columns } from "./wishlist-columns"

export default function WishlistScreen() {
  const wishes:TWish[] = getWishes()

  return (
    <div className="container mx-auto py-10">
      <DataTable columns={columns} data={wishes} />
    </div>
  )
}