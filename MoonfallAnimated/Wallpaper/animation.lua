function get_lines(filename)
    local lines = {}
    for line in io.lines(filename) do
        lines[#lines+1] = line
    end
    return lines
end

function Initialize()

    local pythonPath = SKIN:MakePathAbsolute('HourlyScheduler.py')
    SKIN:Bang('!Execute ["python" "' .. pythonPath .. '"]')

    hour = os.date("%H")
    start = os.clock()

    local framesPath = SKIN:MakePathAbsolute("Resources\\frames.txt")
    frames = get_lines(framesPath)

end

function Update()
    if hour ~= os.date("%H") then
        local pythonPath = SKIN:MakePathAbsolute('HourlyScheduler.py')
        SKIN:Bang('!Execute ["python" "' .. pythonPath .. '"]')

        hour = os.date("%H")
        start = os.clock()

        local framesPath = SKIN:MakePathAbsolute("Resources\\frames.txt")
        frames = get_lines(framesPath)
    end

    local n = math.floor(os.clock() - start) + 1
	SKIN:Bang( '!SetWallpaper', frames[n], 'fit')
end