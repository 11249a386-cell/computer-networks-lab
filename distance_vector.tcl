set ns [new Simulator]
$ns rtproto DV
set nf [open out.nam w]
$ns namtrace-all $nf
set tr [open trace.tr w]
$ns trace-all $tr

proc finish {} {
    global ns nf tr
    $ns flush-trace
    close $nf
    close $tr
    exec nam out.nam &
    exit 0
}

for {set i 0} {$i < 8} {incr i} { set n($i) [$ns node] }
for {set i 0} {$i < 7} {incr i} {
    $ns duplex-link $n($i) $n([expr {$i+1}]) 1Mb 10ms DropTail
}
$ns duplex-link $n(7) $n(0) 1Mb 10ms DropTail

set udp [new Agent/UDP]
$ns attach-agent $n(0) $udp
set null [new Agent/Null]
$ns attach-agent $n(4) $null
$ns connect $udp $null
set cbr [new Application/Traffic/CBR]
$cbr attach-agent $udp
$cbr set packetSize_ 500
$cbr set interval_ 0.005
$ns at 0.0 "$n(0) label Source"
$ns at 0.0 "$n(4) label Destination"
$ns at 0.5 "$cbr start"
$ns rtmodel-at 1.0 down $n(3) $n(4)
$ns rtmodel-at 2.0 up $n(3) $n(4)
$ns at 4.5 "$cbr stop"
$ns at 5.0 "finish"
$ns run
