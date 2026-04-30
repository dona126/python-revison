# async def: defines an async function
# await: waits for this to finish before next line
# asyncio.run(): runs the async function


import asyncio

async def run_test(page):
    print(f"🔄 Testing {page}...")
    await asyncio.sleep(1)        # simulates browser waiting
    print(f"✅ {page} done!")

asyncio.run(run_test("login"))
print("END....1")






# Writing to a file
with open("results.txt", "w") as f:
    f.write("Login Test: Passed\n")
    f.write("Signup Test: Failed\n")

# Reading from a file
with open("results.txt", "r") as f:
    content = f.read()
    print(content)

print("END....2")


# "w" write — creates or overwrites
# "r"read — reads existing file
# "a"append — adds to existing file








import asyncio

async def run_test_suite():
    pages = ["login", "signup", "dashboard"]
    results = []

    for page in pages:
        print(f"🔄 Running {page} test...")
        await asyncio.sleep(0.5)        # simulates browser wait
        results.append(f"{page}: passed")
        print(f"✅ {page} test done!")

    # Save to file
    with open("test_results.txt", "w") as f:
        for result in results:
            f.write(result + "\n")

    print("📄 All results saved to test_results.txt!")

asyncio.run(run_test_suite())
print("END....3")












