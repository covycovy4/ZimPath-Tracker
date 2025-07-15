import subprocess
import os

def run_minimap2(fastq_path, reference_path):
    output_path = fastq_path + ".paf"
    
    cmd = [
        "minimap2",
        "-x", "map-ont",  # Preset for Oxford Nanopore reads (change if needed)
        reference_path,
        fastq_path
    ]
    
    try:
        with open(output_path, "w") as out:
            subprocess.run(cmd, stdout=out, check=True)
        return output_path
    except subprocess.CalledProcessError:
        return None
