import query_executor

def main():
    executor = query_executor.QueryExecutor()
    # executor.executeStringQueryWithResult("INSERT INTO vote VALUES (\'abb\', \'bba\', \'aaa\')")
    executor.executeStringQueryWithoutResult("DROP SCHEMA public CASCADE")
    executor.executeStringQueryWithoutResult("CREATE SCHEMA public")
    executor.executeStringQueryWithoutResult("CREATE TABLE public.test(username varchar(36), age int)")
    executor.executeStringQueryWithoutResult("INSERT INTO test VALUES ('zoewithbigtong', 23)")
    executor.executeStringQueryWithoutResult("INSERT INTO test VALUES ('shentong', 23)")
    resultList = executor.executeStringQueryWithResult("SELECT * FROM test")
    print resultList

if __name__ == '__main__':
    main()