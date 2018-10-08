max_page=$1
if [ ! "$1" ];then
    max_page=5
fi
echo "max_page=${max_page}"

count=10
while [ $count -gt 0 ]; do
    scrapy crawl hupu_post -a max_page=${max_page}
    sleep 600
    count=$((count - 1))
    echo $count
done
echo "end scrawl..."
