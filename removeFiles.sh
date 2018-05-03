function main
{
find *.zip *archive* -mtime +1 -exec rm -r {} \;
}