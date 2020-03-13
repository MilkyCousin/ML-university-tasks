from initial_task.implementation_base import *


def pictures_e_cdf(m=0, s=1, n_l=4, n_u=2000, n_s=4):

    n_steps = (n_u - n_l) // n_s

    x = nr.normal(m, s, n_l)
    z = nr.standard_cauchy(n_l)

    for j in range(n_steps):
        x_f = x[out(x)]
        z_f = z[out(z)]

        e_cdf_x = ECDF(x)
        e_cdf_z = ECDF(z)

        ls_t = np.linspace(min(np.min(x_f), np.min(z_f)), max(np.max(x_f), np.max(z_f)))

        e_x = e_cdf_x(ls_t)
        e_z = e_cdf_z(ls_t)

        fg, a = plt.subplots(1, 1)
        fg.suptitle('Cauchy and Normal Empirical CDF', y=1)
        a.step(ls_t, e_x, color='purple', label='Empirical CDF - Normal', where='post')
        a.step(ls_t, e_z, color='orange', label='Empirical CDF - Cauchy', where='post')
        a.legend()
        plt.savefig('./e_cdf_animated/empirical_cdf_%i.png' % j)
        plt.close()

        x = np.hstack((x, nr.normal(m, s, n_s)))
        z = np.hstack((z, nr.standard_cauchy(n_s)))


def pictures_hist(m=0, s=1, n_l=4, n_u=2000, n_s=4):

    n_steps = (n_u - n_l) // n_s

    x = nr.normal(m, s, n_l)
    z = nr.standard_cauchy(n_l)

    for j in range(n_steps):
        x_f = x[out(x)]
        z_f = z[out(z)]

        plt.hist(x_f, color='violet')
        plt.title('N(%.2f, %.2f) - filtered' % (m, s))
        plt.savefig('./hists_animated/hist_normal_%i.png' % j)
        plt.close()

        plt.hist(z_f, color='orange')
        plt.title('Cauchy - filtered')
        plt.savefig('./hists_animated/hist_cauchy_%i.png' % j)
        plt.close()

        x = np.hstack((x, nr.normal(m, s, n_s)))
        z = np.hstack((z, nr.standard_cauchy(n_s)))


if __name__ == '__main__':

    pictures_e_cdf()
