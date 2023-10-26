# Allocate and Manage Memory

## On The System Level

In modern operating systems, processes request and utilize virtual memory on the highest level. The operating system manages the virtual memory for each process. It maps those actually used virtual memory pages to physical memory pages backed by hardware (like DDR4 RAM sticks). It is important to note that a process may request a lot of virtual memory space but may merely use a small portion of it. **For example, a process can always successfully claim, say, 2TB of virtual memory from the operating system even though the system may only have 8GB of RAM. This will go without any problems as long as that process does not write to too many memory pages of this huge virtual memory space**. It is this potentially small portion of the virtual memory space that will actually get mapped to the physical memory devices and thus is what we really care about. **So never panic when you see large virtual memory usage (usually named VIRT) in tools like ps and top**.

**The small portion of the virtual memory which is actually used (meaning written data to) is usually called RSS or resident memory**. Well, when the system is running out of physical memory and some part of the resident memory gets swapped out to the disk1, then this swapped-out portion is no longer part of the resident memory and becomes the **“swapped memory” (or “swap” for short)**.

Note:
---
> Three types of memories: VIRT, RSS and swap 

## Nginx Shared Memory (short as shm)

Shared memory zones are allocated via the mmap() system call directly and thus bypassing the standard C library’s allocator completely.Nginx shared memory zones are shared among all its worker processes. 

For example, Nginx’s standard modules **ngx_http_limit_req** and **ngx_http_limit_conn** use shared memory zones to hold state data to limit the client request rate and client requests' concurrency level across all the worker processes. OpenResty’s ngx_lua module provides **lua_shared_dict** to provide shared memory dictionary data storage for the user Lua code.

**Nginx’s shared memory zones may take much less physical memory resources than the size configured in the nginx.conf file**. Thanks to the **demand-paging** feature of modern operating systems. We demonstrated that empty shared memory zones may still utilize some memory pages and slabs to store the slab allocator’s meta data. 

### HUP reload

Any attempts to use HUP reload to release up shared memory zones' existing resident memory pages would fail. The user should use full restart or Nginx’s binary upgrade operation instead

### Memory Fragmentation

1. Always use similarly sized data entries so that there won’t be the problem of accommodating future larger memory block requests in the first place.
2. Making deleted entries adjacent to each other so that they can merge into larger free slabs.

For 1), we can divide a single monolithic zone into several zones for different entry size groups2. For example, we can have a zone dedicated for data entries of the 0 ~ 128 byte size range only, and another for the 128 ~ 256 byte range.

For 2), we can group entries by their expiration time. Short-lived entries can live in a dedicated zone while long-lived entries live in another zone. This helps entries expire in a similar pace, increasing the chance of getting expired and eventually deleted at the same time.


